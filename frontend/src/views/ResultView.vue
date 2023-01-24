<template>
  <div class="result">
    <div class="home__page">
      <div class="home__page-name">
        <h2>{{ positions[0].product_query_name }}</h2>
      </div>
    </div>

    <div class="home__forms-title home__title"><span>Все результаты по запросу: "{{
        positions[0].product_query_name
      }}"</span></div>
    <!--    <GenerateCP v-if="isVisible" v-model="responseData" />-->
    <div class="home__forms-table" v-if="isVisible">
    <textarea class="home__generate_cp" v-model="responseData[0].product_query_name" cols="50" rows="20">
    </textarea>
    </div>
    <div class="home__forms-body">
      <div class="positions-forms">
        <div class="position-form" v-for="product in positions" v-bind:key="product.id">

          <div style="display: none">{{ product.id }}</div>
          <div class="position__img">
            <a :href="product.product_link" target="_blank">
              <img :src="product.product_link_img" alt="" width="200" height="200">
            </a>
          </div>

          <div class="position__body">
            <div class="position__name">
              <a :href="product.product_link" target="_blank">{{ product.product_scrap_name }}</a>
            </div>
            <div class="position__quality">
              <template v-if="product.product_quality">
                Состояние: {{ product.product_quality }}
              </template>
              <template v-else>
                <span style="color:#b90012;">Состояние: Неизвестно</span>
              </template>
            </div>
            <div class="position__city">
              <template v-if="product.product_platform === 'Ebay' || product.product_platform === 'AliExpress'">
                Страна: {{ product.product_country }}
              </template>
              <template v-else-if="product.product_platform === 'Avito'">
                Город: {{ product.product_country }}
              </template>
            </div>
            <div class="position__platform">Платформа: {{ product.product_platform }}</div>
          </div>

          <div class="position__cp">
            <div class="position__price">{{ product.product_price }}</div>
            <div class="cp__bu">
              <input class="cp-input" :id="'cp-input-bu_' + product.id" type="checkbox" name="bu"
                     :value="product.id">
              <label :for="'cp-input-bu_' + product.id">как Б/У</label>
            </div>
            <div class="cp__new">
              <input class="cp-input" :id="'cp-input-new_' + product.id" type="checkbox" name="news"
                     :value="product.id">
              <label :for="'cp-input-new_' + product.id">как новый</label>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div style="display: flex; align-items: center;">
      <button class="home__generate-offer button" @click="generateCP">Сформировать КП</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ResultView',
  currentPage: 'result',

  props: {
    msg: String,
  },
  data() {
    return {
      positions: [{}],
      quality_checkbox: {
        bu: false,
        new: false
      },
      isVisible: false,
      responseData: ''
    }
  },
  created() {
    const id = this.$route.params.id;
    axios.post(`http://localhost:8000/api_result/${id}/`,
        {
          query_id: id,
          user: 'ПростойРаботяга'
        })
        .then(response => {
          this.positions = response.data
        })
  },
  methods: {
    showResponse(dataBu, dataNew) {
      console.log(dataBu)
      console.log(dataNew)
      this.responseData = dataBu;
      this.isVisible = true;
    },
    generateCP() {
      const bu = []
      const neww = []
      const buCheckboxes = document.querySelectorAll('input[name="bu"]:checked')
      const newCheckboxes = document.querySelectorAll('input[name="news"]:checked')
      buCheckboxes.forEach(checkbox => {
        if (checkbox.checked) {
          bu.push(checkbox.value)
        }
      })
      newCheckboxes.forEach(checkbox => {
        if (checkbox.checked) {
          neww.push(checkbox.value)
        }
      })
      axios.post('http://localhost:8000/api_generate_cp/', {
        bu: bu,
        new: neww
      })
          .then(response => {
            // console.log(response.data);
            this.showResponse(response.data.bu, response.data.new);
          })
    }
  }
}
</script>

<style scoped>

</style>