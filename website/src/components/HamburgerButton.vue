<template>
  <button class="hamburger" aria-label="Menu" @click="$emit('hamburger')">
    <span class="hamburger-container" tabindex="-1">
      <span class="hamburger-bars"></span>
    </span>
  </button>
</template>

<script>
export default {
  name: 'HamburgerButton',
  methods: {},
};
</script>

<style lang="scss" scoped>
  .hamburger {
    margin: 0;
    padding: 0;
    border: 0;
    background-color: transparent;
    cursor: pointer;

    &:focus {
      & > .hamburger-container {
        box-shadow: 0 0 2px 2px #51a7e8;
      }
    }
  }

  .hamburger-container {
    display: flex;
    align-items: center;
    position: relative;
    width: 35px;
    height: 30px;
  }

  .hamburger-bars {
    position: absolute;
    width: 35px;
    height: 2px;
    background-color: #000;
    transition: transform 220ms ease-in-out;

    &:before, &:after {
      content: '';
      display: block;
      position: absolute;
      width: 35px;
      height: 2px;
      background-color: #000;
    }

    &:before {
      top: -12px;
      transition: top 100ms 250ms ease-in, transform 220ms ease-in-out;
    }

    &:after {
      bottom: -12px;
      transition: bottom 100ms 250ms ease-in, transform 220ms ease-in-out;
    }
  }

  .hamburger-active {
    .hamburger-bars {
      transform: rotate(225deg);
      transition: transform 220ms 120ms ease-in-out;

      &:before {
        top: 0;
        transition: top 100ms ease-out;
      }

      &:after {
        bottom: 0;
        transform: rotate(-90deg);
        transition: bottom 100ms ease-out, transform 220ms 120ms ease-in-out;
      }
    }
  }

  .hamburger, .hamburger-container {
    &:focus {
      outline: none;
    }
  }
</style>
