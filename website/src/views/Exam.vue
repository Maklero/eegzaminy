<template>
  <div class="exam">
    {{ examData }}
  </div>
</template>

<script>
import axios from 'axios';
import dataFile from '@/api.json';

const API = dataFile.url;

export default {
  name: 'Exam',
  data() {
    return {
      examName: null,
      examData: null,
    };
  },
  mounted() {
    this.examName = this.$route.params.name;
    axios.get(`${API}/exams/${this.examName}`)
      .then((response) => {
        this.examData = response;
      })
      .catch((error) => {
        console.error(error);
      });
  },
};
</script>

<style lang="scss" scoped>

</style>
