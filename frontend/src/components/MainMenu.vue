<template>
  <header class="header">
    <div class="header__body">
      <div class="header__nav">
        <div class="header__logo"><a href="/"><img class="logo" src="../assets/logo.png" width="40"></a></div>
        <div class="header__nav-links">
          <router-link class="header__nav-link" v-bind:class="{ 'is-active': currentPage === 'home' }" to="/"
             @click="currentPage = 'home'">Поиск</router-link>
          <router-link class="header__nav-link" v-bind:class="{ 'is-active': currentPage === 'results' }" to="/results/"
             @click="currentPage = 'result'">Результаты</router-link>
          <router-link class="header__nav-link" v-bind:class="{ 'is-active': currentPage === 'settings' }" to="/settings/"
             @click="currentPage = 'settings'">Управление</router-link>
        </div>
      </div>
      <div class="header__visitor"><span></span>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'MainMenu',
}
</script>

<style scoped>

</style>