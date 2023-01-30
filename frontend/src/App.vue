<template>
  <MainMenu/>
  <router-view/>
</template>

<script>
import MainMenu from '@/components/MainMenu.vue'

export default {
  components: {
    MainMenu
  }
}
</script>

<style lang="scss">
// COLORS
$color-black: #000;
$color-white: #fff;
$color-gray: #eee;
$color-light-gray: #ccc;

// FONTS
// stylelint-disable-next-line
$font-primary: -apple-system, blinkmacsystemfont, "Segoe UI", roboto, oxygen, ubuntu, cantarell, "Open Sans", "Helvetica Neue", sans-serif;

// EASING TRANSITIONS
$duration-normal: 0.4s;
$easing-back-out: cubic-bezier(0.25, 0.74, 0.22, 1.1); // http://cubic-bezier.com/#.25,.74,.22,1.1
$easing-back-in: cubic-bezier(0.47, -0.1, 0.5, -0.06); // http://cubic-bezier.com/#.47,-0.1,.5,-.06
$easing-out: ease-out;
$easing-in: ease-in;

// Settings
$desktop: 1205;
$desktop-xl: 1800;
$laptop: 1440;
$tablet: 768;
$mobile: 320;
$desktop-vh: 750;


* {
  margin: 0;
  padding: 0;
}

*, *:before, *:after {
  -webkit-box-sizing: inherit;
  box-sizing: inherit;
}

html {
  overflow-x: hidden;
  min-height: 100vh;
  -webkit-box-sizing: border-box;
  /* box-sizing: border-box; */
  font-family: -apple-system, blinkmacsystemfont, "Segoe UI", roboto, oxygen, ubuntu, cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  background-color: rgba(0, 0, 0, 0.05);
  scroll-behavior: smooth;
}

a {
  text-decoration: none;
  color: currentColor;
}

h2 {
    display: block;
    font-size: 1.5em;
    margin-block-start: 0.83em;
    margin-block-end: 0.83em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    font-weight: bold;
}

.header {
  border-bottom: 1px solid #ccc;
  padding: 8px 0;
  background-color: $color-white;

  &__nav {
    display: flex;
    align-items: center;

    &-link {
      margin: 0 20px;
      padding: 22px 0;

      &:hover {
        border-bottom: 3px solid rgba(59, 130, 246, 0.5);
      }
    }

    .router-link-exact-active {
      border-bottom: 3px solid rgba(59, 130, 246, 0.5);
    }
  }

  &__body {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: 0 auto;
    max-width: 80rem;
  }

  &__list {
    width: 100%;
    text-align: center;
  }

  &__link {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: left;
    margin: 0 auto;
    padding: 10px 30px;
    min-height: 85px;
    font-weight: 700;
    font-size: 16px;
    line-height: 25px;
    text-align: left;
    color: rgba($color-black, 0.7);
    background-color: $color-white;

    &:not(:last-child) {
      border-bottom: 1px solid $color-gray;
    }

    &:first-child {
      border-top: 1px solid $color-gray;
    }
  }

  &__burger {
    z-index: 100;
    flex-direction: column;
    margin: (-6.5px / 2) 0;
    margin-left: auto;
    width: 39px;
    color: $color-black;

    span {
      display: block;
      margin: 6.5px 0;
      width: 39px;
      height: 2px;
      background-color: currentColor;
      transition: $duration-normal;
    }
  }
}


.button {
  border: 0;
  border-radius: 0.5rem;
  padding: 10px 24px;
  color: $color-white;
  background: #6c757d;
  transition: 0.2s;
  cursor: pointer;

  &:hover {
    background: #495057;
  }

  &:active {
    background: #343a40;
  }
}

.home, .result {
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-weight: 500;

  .login {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 70vh;

    form {
      padding: 30px;

      .errorlist {
        color: #c52c2c;
      }

      .helptext {
        display: none;
      }

      p {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 15px 0;
      }

      label {
        margin-right: 30px;
      }

      input[type='text'], input[type='password'], input[type='email'] {
        border: 1px solid #ccc;
        padding: 6px 12px;
        border-radius: 0.5rem;
      }
    }

    .register {
      margin: 15px 0;
      font-weight: 100;
    }
  }

  .all-forms {
    border-radius: 0.5rem;
    padding: 16px;
    max-width: 80rem;
    background: #fff;
  }

  &__title {
    margin: 0 auto;
    border-bottom: 1px solid $color-light-gray;
    border-radius: 0.5rem 0.5rem 0 0;
    padding: 16px;
    max-width: 80rem;
    background: $color-white;
  }

  &__page {
    background: $color-white;

    &-name {
      margin: 0 auto;
      padding: 3px 55px;
      max-width: 80rem;
    }
  }

  &__search-form {
    margin: 72px auto 0;
    border-radius: 0.5rem;
    max-width: 80rem;
    background: $color-white;

    &-body {
      display: flex;
      justify-content: center;
      padding: 12px;
    }

    &__input,
    &__button {
      border: 1px solid $color-light-gray;
      padding: 6px 12px;
    }

    &__input {
      border-radius: 0.5rem 0 0 0.5rem;
      width: 85%;
      font-weight: 500;
      font-size: 23px;
    }

    &__button {
      border-radius: 0 0.5rem 0.5rem 0;
    }
  }

  &__settings {
    margin: 24px auto 0;
    border-radius: 0.5rem;
    padding: 16px;
    max-width: 80rem;
    background: $color-white;

    &-text {
      padding-right: 16px;
    }
  }

  &__generate-offer {
    position: fixed;
    right: 0;
    bottom: 0;
    z-index: 10;
    margin: 0 2em 2em 0;
    box-shadow: 0 0 10px $color-black;
  }

  &__setting {
    margin-top: 15px;
    border-top: 1px #ccc solid;
  }

  &__platform-scrap {
    display: flex;
    justify-content: space-around;
    margin: 15px 0 0;

    &-platform {
      cursor: pointer;

      input,
      label {
        cursor: pointer;
      }
    }
  }

  &__forms-title {
    margin: 24px auto 0;
  }

  &__forms-body {
    max-width: 80rem;
    margin: 0 auto;
    background: #fff;
  }

  &__generate_cp {
    border: 1px solid $color-light-gray;
    border-radius: 0.5rem;
    padding: 6px 12px;
  }

  &__forms-settings, &__forms-delivery_time {
    margin: 0 auto;
    border-radius: 0 0 0.5rem 0.5rem;
    padding: 10px 10px 30px;
    max-width: 80rem;
    background: $color-white;
  }

  &__forms-table {
    margin: 0 auto;
    border-radius: 0 0 0.5rem 0.5rem;
    padding: 10px 10px 30px;
    max-width: 80rem;
    background: $color-white;

    table {
      border-collapse: collapse;
      width: 100%;

      td {
        padding: 15px;
        text-align: center;
      }
    }

    thead tr {
      background: #a1a9b1;
    }

    tbody .platforms {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      margin: 0 auto;
      width: 15%;

      p {
        padding: 2px 0;
      }
    }

    tbody tr:nth-child(odd) {
      background-color: #e9ecef;
    }

    tbody tr:nth-child(even) {
      background-color: #dee2e6;
    }

    tbody .for-view {
      display: flex;
      justify-content: center;
    }
  }

  .home__forms-settings {
    display: flex;

    .settings-block {
      display: flex;
      flex-direction: column;
      margin: 0 10px;

      input, textarea {
        border-radius: 0.5rem;
        width: 85%;
        font-weight: 500;
        font-size: 23px;
        border: 1px solid #ccc;
        padding: 6px 12px;
      }

      &:first-child {
        margin: 0;
      }
    }
  }

  .positions-forms {
    padding: 16px;
  }

  .position-form {
    display: flex;
    margin: 1em;
    border: 2px $color-light-gray solid;
    border-radius: 15px;
    background-color: #fff;

    .position__img,
    .position__body {
      margin: 0.5em;
    }

    .position__img {
      overflow: hidden;
      border: 1px $color-light-gray solid;
      border-radius: 15px;
      height: 200px;
      min-width: 200px;
      color: $color-light-gray;

      img {
        max-width: 200px;
        max-height: 200px;
        object-fit: cover;
      }
    }

    .position__body-cp {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
    }

    .position__body {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      width: 45em;
      font-size: 18px;

      .position__name {
        font-size: 25px;
        color: #30b9ff;
        transition: all 0.2s ease;

        a:hover {
          text-decoration: underline;
          transition: all 0.2s ease;
        }
      }
    }

    .position__price {
      font-size: 18px;
    }

    .position__cp {
      display: flex;
      flex-direction: column;
      justify-content: space-evenly;
      border-left: 1px $color-light-gray solid;
      padding-left: 10px;
      width: 10em;
      min-width: 10em;

      .cp__bu,
      .cp__new {
        display: flex;
      }

      .cp-input {
        margin-right: 5px;
        transform: scale(1.5);
        cursor: pointer;
      }

      .cp__bu label,
      .cp__new label {
        margin: 5px;
        font-size: 18px;
        cursor: pointer;
      }
    }
  }
}


#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  //text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
