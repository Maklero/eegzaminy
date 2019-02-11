<template>
  <div id="app">
    <div class="menu-clicker" @click="menuAction">
      <div></div>
      <div></div>
      <div></div>
    </div>
    <div id="nav">
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

const API = 'http://192.168.8.118:8080/v1';

function menuExpander(event, skip = false) {
  if (skip === true) return; // TODO Why doesn't work just `if (skip)`?
  const nav = document.querySelector('#nav');
  if (nav.style.opacity === '0' || nav.style.opacity === '') {
    nav.style.display = 'flex';
    setTimeout(() => { nav.style.opacity = '1'; }, 1);
  } else {
    nav.style.opacity = '0';
    setTimeout(() => { nav.style.display = 'none'; }, 300);
  }
}

export default {
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
    menuAction: menuExpander,
  },
  watch: {
    $route() {
      // TODO close navigation without changing url
      menuExpander();
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
    display: flex;
    flex-direction: column;
    justify-content: center; align-items: center;
    width: 50px; height: 50px;
    background-color: #455A64;
    border-radius: 50%;
    position: fixed;
    top: 5px; left: 5px;
    z-index: 10;

    div {
      width: 37px;
      border: 1.5px solid white;
      margin: 3px 0;
    }
  }

  #nav {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100vh;
    padding-top: 60px;
    display: none;
    flex-direction: column;
    align-items: center;
    font-size: 2em;
    background-color: #455A64;
    z-index: 9; opacity: 0;
    transition: opacity .15s;
  }

  a {
    color: white;
    text-decoration: none;
    transition: color .15s;

    &:hover {
      color: wheat;
    }
  }

  .content {
    width: 100%;
    min-height: 100vh;
  }
</style>
