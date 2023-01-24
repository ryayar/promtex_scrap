<template>
    <div class="home__page">
      <div class="home__page-name">
        <h2>Поиск</h2>
      </div>
    </div>
    <SearchForm/>
    <div class="home__forms-title home__title"><span>Последние 10 результатов</span></div>
    <ResultsForm msg="home"/>
</template>

<script>
// @ is an alias to /src
import SearchForm from '@/components/SearchForm.vue'
import ResultsForm from '@/components/ResultsForm.vue'

export default {
  name: 'HomeView',
  components: {
    SearchForm,
    ResultsForm
  }
}
</script>
