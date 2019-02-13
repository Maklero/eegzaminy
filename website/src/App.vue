<template>
  <div id="app">
    <div class="menu-clicker">
      <HamburgerButton @hamburger="hamburger" />
    </div>
    <div class="nav">
      <router-link to="/">Home</router-link>
      <router-link to="/about">About</router-link>
      <router-link
        v-for="exam in examList"
        :to="`/${exam.route}`"
        :key="exam.route">
        {{ exam.content }}
      </router-link>
    </div>
    <router-view class="content"/>
  </div>
</template>

<script>
import axios from 'axios';
import HamburgerButton from '@/components/HamburgerButton.vue';

const API = 'http://127.0.0.1:8080/v1';

export default {
  components: { HamburgerButton },
  data() {
    return {
      examList: [],
    };
  },
  mounted() {
    axios.get(`${API}/exams/list`)
      .then((response) => {
        const res = response.data.list;
        res.forEach((r) => {
          this.examList.push({
            route: `exam/${r}`,
            content: r.toUpperCase(),
          });
        });
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {
    hamburger: () => {
      const menu = document.querySelector('.hamburger');
      const nav = document.querySelector('.nav');

      menu.classList.toggle('hamburger-active');
      nav.classList.toggle('nav-open');
    },
  },
};
</script>

<style lang="scss">
  body {
    margin: 0;
    padding: 0;
  }

  * {
    box-sizing: border-box;
  }

  .menu-clicker {
    position: fixed;
    top: 10px;
    left: 10px;
  }

  .nav {
    display: none;
    flex-direction: column;
    padding-top: 60px;
    align-items: center;
    width: 100%;
    height: 100vh;
    font-size: 2.5em;
    opacity: 0;
    background-color: #455A64;
  }

  .nav-open {
    display: flex;
    opacity: 1;
    animation: opacity 220ms;
  }

  @keyframes opacity {
    from { opacity: 0;}
    to { opacity: 1 }
  }

  a {
    color: white;
    text-decoration: none;
  }
</style>
