<template>
  <div class="home">
    <div class="home__page">
      <div class="home__page-name">
        <h2>Настройки</h2>
      </div>
    </div>
    <div class="home__forms-title home__title"><span>Настройки</span></div>
    <div class="home__forms-table">
        <table>
          <col style="width:20%">
          <col style="width:20%">
          <col style="width:20%">
          <col style="width:40%">
          <thead>
          <tr>
            <td>Страна</td>
            <td>Срок поставки (дни)</td>
            <td>Срок поставки (текст)</td>
            <td>Управление</td>
          </tr>
          </thead>
          <tbody>
          <tr v-for="item in items" :key="item.id">
            <td v-if="item.isEdit"><input v-model.trim="item.country" type="text"></td>
            <td v-else><span>{{ item.country }}</span></td>
            <td v-if="item.isEdit"><input v-model.trim="item.delivery_time_days" type="number"></td>
            <td v-else><span>{{ item.delivery_time_days }}</span></td>
            <td v-if="item.isEdit"><input v-model.trim="item.delivery_time_text" type="text"></td>
            <td v-else><span>{{ item.delivery_time_text }}</span></td>
            <td>
              <button v-if="item.isEdit" class="secd button" @click="saveItem(item.id)">Сохранить</button>
              <button v-else class="secd button" @click="editItem(item.id)">Изменить</button>
              <button v-if="item.isEdit" class="secd button" @click="cancelEdit(item.id)">Отменить</button>
              <button v-else class="secd button" @click="deleteItem(item.id)">Удалить</button>
            </td>
          </tr>
          </tbody>
        </table>
      <button class="button" style="margin: 40px 0 0" id="add-button" @click="addItem">Добавить строку</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'SettingsView',
  data() {
    return {
      items: [],
      newItem: []
    }
  },
  created() {
    axios.post('http://193.187.96.247:8000/api_settings/')
        .then(response => {
          this.items = response.data
        })
  },
  methods: {
    addItem() {
      this.items.push({
        country: '',
        delivery_time_days: 0,
        delivery_time_text: '',
        isEdit: true,
      })
    },
    editItem(id) {
      const item = this.items.find(item => item.id === id);
      item.isEdit = true;
      this.previousCountry = item.country
      this.previousDeliveryTimeDays = item.delivery_time_days
      this.previousDeliveryTimeText = item.delivery_time_text
      this.country = item.country
      this.delivery_time_days = item.delivery_time_days
      this.delivery_time_text = item.delivery_time_text
    },
    cancelEdit(id) {
      const item = this.items.find(item => item.id === id);
      item.isEdit = false
      item.country = this.previousCountry
      item.delivery_time_days = this.previousDeliveryTimeDays
      item.delivery_time_text = this.previousDeliveryTimeText
    },
    saveItem(id) {
      const item = this.items.find(item => item.id === id);
      item.isEdit = false;
      axios.post(`http://193.187.96.247:8000/api_save_item/`, {
            id: id,
            country: item.country,
            delivery_time_days: item.delivery_time_days,
            delivery_time_text: item.delivery_time_text
          },
          {headers: {'Content-Type': 'application/json'}})
          .then(response => {
            if (response.data.createSuccess) {
              location.reload()
            }
          })
    },
    deleteItem(id) {
      axios.post(`http://193.187.96.247:8000/api_delete_item/${id}/`, {
        query_id: id,
      })
          .then(response => {
            if (response.data.success) {
              location.reload();
            }
          })
    },
  }
}
</script>

<style scoped>
.secd {
  margin: 0 7px;
}
</style>