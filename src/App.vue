<script>
import Questionnaire from './components/Questionnaire.vue'
import axios from 'axios'

let data= []

export default {
  name: 'App',
  mounted(){
    this.loadDB();
  },

  methods:{
    async loadDB(){

      data = await axios.get('http://localhost:5000/');
      data = data.data.questionnaires;
      console.log(data);
    },
    afficherTousLesQuestionnaires(){
      this.questionnaires.forEach(questionnaire => {
        console.log(questionnaire.data);
      });
    },
  
    creerQuestionnaire(){

    },

    supprimerQuestionnaire(){

    },

    modifierQuestionnaire(){

    }
  },

  components: { Questionnaire }
}

</script>

<template>
  <body>
    <div>
      <h1>Application</h1>
      <img class="images" src="/img/10738849-autocollant-d-un-signe-de-quiz-de-dessin-anime-vectoriel.jpg">
    </div>
    
    <h2>Questionnaires disponibles :</h2>
    <di>
      <Questionnaire v-for="questionnaire in data" :key="questionnaire.id" :Questionnaire="questionnaire"/>    </di>
  </body>
  <footer>BABA Ahmet - CHHUM--MOXEL Loann</footer>
</template>

<style>
html{
  justify-content: center;
}
body {
  display: flex;
  flex-wrap: wrap;
}
.images{
  height: 10vh;
}

</style>
