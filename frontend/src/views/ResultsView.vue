<template>
  <div class="home__page">
    <div class="home__page-name">
      <h2>Результаты</h2>
    </div>
  </div>
  <SearchForm/>
  <div class="home__forms-title home__title"><span>Все запросы</span></div>
  <ResultsForm msg="results"/>

</template>

<script>
import ResultsForm from '@/components/ResultsForm.vue'
import SearchForm from '@/components/SearchForm.vue'

export default {
  name: 'ResultsView',
  components: {
    ResultsForm,
    SearchForm
  }
}
</script>

<style scoped>

</style>