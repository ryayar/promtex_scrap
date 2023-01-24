<template>
  <div class="home__forms-table">
    <table>
      <col style="width:25%">
      <col style="width:25%">
      <col style="width:25%">
      <col style="width:25%">
      <thead>
      <tr>
        <td>Запрос</td>
        <td>Платформы</td>
        <td>Дата</td>
        <td>Результат</td>
      </tr>
      </thead>
      <tbody>
      <tr v-for="query in queries" v-bind:key="query.id">
        <td>{{ query.product_query_name }}</td>
        <td>
          <div class="platforms">
            <p>{{ query.product_platform }}</p>
          </div>
        </td>
        <td>{{ query.query_date }}</td>
        <td>
          <div class="for-view">
            <a :href="'/result/' + query.query_id + '/'">
              <div class="button">Просмотр</div>
            </a>
          </div>
        </td>
      </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  name: 'ResultsForm',
  props: {
    msg: String,
  },
  data() {
    return {
      queries: [
        {}
      ]
    }
  },
  created() {
    if (this.msg === 'home') {
      axios.post('http://localhost:8000/api_index/')
          .then(response => {
            this.queries = response.data
          })
    }
    if (this.msg === 'results') {
      axios.post('http://localhost:8000/api_results/')
          .then(response => {
            this.queries = response.data
          })
    }
  }
}
</script>
