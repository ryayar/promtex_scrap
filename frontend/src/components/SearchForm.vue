<template>
  <form @submit.prevent="submitForm">
    <div class="home__search-form">
      <div class="home__search-form-title home__title">
        <span>Поиск</span>
      </div>
      <div class="home__search-form-body">
        <input class="home__search-form__input" v-model.trim="query" type="text" name="query">
        <input class="home__search-form__button button" type="submit" value="Поиск">
      </div>
      <div v-if="loading" class="loading-overlay">
        <div class="loading-spinner"></div>
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
      loading: false,
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
      this.loading = true;
      axios.post('http://193.187.96.247:8000/api_create/', {
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


<style>
.loading-overlay {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 999;
  display: flex;
  align-items: center;
  justify-content: center;
}

.loading-spinner {
  width: 50px;
  height: 50px;
  border: 2px solid #fff;
  border-top-color: #3498db;
  border-radius: 50%;
  animation: spin 1s ease-in-out infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
</style>

<!--<style scoped>-->
<!--.loading-overlay {-->
<!--  position: fixed;-->
<!--  top: 0;-->
<!--  left: 0;-->
<!--  right: 0;-->
<!--  bottom: 0;-->
<!--  background: rgba(255, 255, 255, 0.8);-->
<!--  z-index: 999;-->
<!--}-->

<!--.loading-spinner {-->
<!--  position: absolute;-->
<!--  top: 50%;-->
<!--  left: 50%;-->
<!--  transform: translate(-50%, -50%);-->
<!--  width: 50px;-->
<!--  height: 50px;-->
<!--  border: 2px solid #fff;-->
<!--  border-top-color: #3498db;-->
<!--  border-radius: 50%;-->
<!--  animation: spin 1s ease-in-out infinite;-->
<!--}-->

<!--/*.loading {*/-->
<!--/*  position: fixed;*/-->
<!--/*  left: 0;*/-->
<!--/*  top: 0;*/-->
<!--/*  width: 100%;*/-->
<!--/*  height: 100%;*/-->
<!--/*  background-color: rgba(0, 0, 0, 0.5);*/-->
<!--/*  z-index: 999;*/-->
<!--/*  display: flex;*/-->
<!--/*  align-items: center;*/-->
<!--/*  justify-content: center;*/-->
<!--/*}*/-->

<!--.loading-spinner {-->

<!--}-->

<!--@keyframes spin {-->
<!--  to { transform: rotate(360deg); }-->
<!--}-->

<!--/*.slide-fade-enter-active {*/-->
<!--/*  transition: all .5s ease;*/-->
<!--/*}*/-->

<!--/*.slide-fade-leave-active {*/-->
<!--/*  transition: all .5s cubic-bezier(1.0, 0.5, 0.8, 1.0);*/-->
<!--/*}*/-->

<!--/*.slide-fade-enter-to, .slide-fade-leave-to {*/-->
<!--/*  transform: translateY(-10px);*/-->
<!--/*  opacity: 0;*/-->
<!--/*}*/-->
<!--</style>-->