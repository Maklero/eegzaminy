<template>
  <div class="question-container">
    <div class="question">
      <h3>Pytanie {{ index + 1 }}</h3>
      <span>{{ question.question }}</span>
    </div>
    <div v-if="question.img">
      <img :src="question.img" :alt="question.img">
    </div>
    <div v-for="(label, index) in names" class="answer">
      <input
        type="radio"
        :name="question.id"
        :value="label"
        :id="`o${index}_${question.id}`"
      >
      <label :for="`o${index}_${question.id}`">
        {{ label }}. {{ question[label] }}
      </label>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Question',
  props: {
    question: {
      type: Object,
      required: true,
    },
    index: {
      type: Number,
      required: true,
    },
    names: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style lang="scss" scoped>
  .question-container {
    flex-direction: column;
    margin: 4px 0;
    width: 98%;
    min-height: 100px;
    overflow: hidden;

    img {
      width: 100%;
    }
  }

  .question, .answer, span, .question-container {display: flex}

  .question, .answer {
    border-radius: 2px;
    padding: 7px;
  }

  .question {
    flex-direction: column;
    min-height: 100px;
    background-color: #90A4AE;

    h3 {
      margin: 0;
      width: 100%;
      height: 30px;
    }

    &, span {
      align-items: center;
      justify-content: center;
    }
  }

  .answer {
    padding: 0;
    margin: 2px 0 0 0;
    width: 100%;
    min-height: 50px;
    flex-direction: row;
    align-items: center;
    background-color: #455A64;

    input[type=radio] {
      margin: 0;
      width: 40px;
    }

    label {
      display: flex;
      align-items: center;
      width: 100%;
      min-height: 50px;
      padding: 5px;
    }
  }
</style>
