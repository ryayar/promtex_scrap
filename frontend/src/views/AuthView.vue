<template>
  <div class="auth-form">
    <h2 class="auth-form__title">Авторизация</h2>
    <form @submit.prevent="submitForm">
      <div class="auth-form__field">
        <label for="email">Email</label>
        <input v-model="email" type="email" id="email" name="email">
      </div>
      <div class="auth-form__field">
        <label for="password">Пароль</label>
        <input v-model="password" type="password" id="password" name="password">
      </div>
      <div class="auth-form__field">
        <button type="submit" :disabled="!isValid">Войти</button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'AuthView',
  data() {
    return {
      email: '',
      password: '',
    }
  },
  computed: {
    isValid() {
      return this.email.length > 0 && this.password.length > 0
    }
  },
  methods: {
    submitForm() {
      if (this.isValid) {
        // send data to server
      } else {
        alert('Заполните все поля')
      }
    }
  }
}
</script>

<style>
.auth-form {
  width: 50%;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
}

.auth-form__field {
  margin-bottom: 10px;
}

.auth-form__title {
  text-align: center;
}
</style>