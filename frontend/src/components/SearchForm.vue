<template>
  <form @submit.prevent="submitForm">
    <div class="home__search-form">
      <div class="home__search-form-title home__title">
        <span>Поиск</span>
      </div>
      <div class="home__search-form-body">
        <input class="home__search-form__input" v-model="query" type="text" name="query">
        <input class="home__search-form__button button" type="submit" value="Поиск">
      </div>
    </div>
    <div class="home__settings">
      <div style="display: flex; align-items: center;">
        <span class="home__settings-text">Настройки</span>
        <div @click="toggleSettings" class="home__settings-form button">
          {{ showSettings ? 'Скрыть' : 'Показать' }}
        </div>
      </div>
      <transition name="slide-fade">
        <div v-if="showSettings" class="home__setting">
          <div class="home__platform-scrap">
            <div class="home__platform-scrap-platform">
              <input class="home__platform-scrap-input" id="platform-ebay" v-model="platforms.ebay" type="checkbox"
                     name="ebay" value="checked">
              <label for="platform-ebay">Ebay</label>
            </div>
            <div class="home__platform-scrap-platform">
              <input class="home__platform-scrap-input" id="platform-ali" v-model="platforms.ali" type="checkbox"
                     name="ali" value="checked">
              <label for="platform-ali">AliExpress</label>
            </div>
            <div class="home__platform-scrap-platform">
              <input class="home__platform-scrap-input" id="platform-avito" v-model="platforms.avito" type="checkbox"
                     name="avito" value="checked">
              <label for="platform-avito">Avito</label>
            </div>
          </div>
        </div>
      </transition>
    </div>
  </form>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SearchForm',
  data() {
    return {
      query: '',
      platforms: {
        ebay: false,
        ali: false,
        avito: false
      },
      showSettings: false
    }
  },
  methods: {
    toggleSettings() {
      this.showSettings = !this.showSettings
    },
    submitForm() {
      if (!this.platforms.ebay && !this.platforms.ali && !this.platforms.avito) {
        alert('Необходимо выбрать хотя бы одну платформу!')
        return
      }
      if (!this.query) {
        alert('Поле поиска не может быть пустым!')
        return
      }

      axios.post('http://localhost:8000/api_create/', {
            query: this.query,
            ebay: this.platforms.ebay,
            ali: this.platforms.ali,
            avito: this.platforms.avito,
            user: 'ПростойРаботяга'
          },
          {headers: {'Content-Type': 'application/json'}})
          .then(response => {
            if (response.status === 200) {
              location.reload();
            }
          })
    }
  }
}
</script>

<style scoped>
/*.slide-fade-enter-active {*/
/*  transition: all .5s ease;*/
/*}*/

/*.slide-fade-leave-active {*/
/*  transition: all .5s cubic-bezier(1.0, 0.5, 0.8, 1.0);*/
/*}*/

/*.slide-fade-enter-to, .slide-fade-leave-to {*/
/*  transform: translateY(-10px);*/
/*  opacity: 0;*/
/*}*/
</style>