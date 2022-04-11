<template>
  <BlogHeader/>
  <div id="app" align="center"><h1>{{msg}}</h1></div>

  <div class="qa" align="center">
        <form>
            <input v-model="qaTag" type="text" placeholder="输入qa内容...">
            <div>qaTag:{{qaTag}}</div>
            <button v-on:click.prevent="getNameResponde">提交</button>
            <p>Name Response from backend: {{ nameResponse }}</p>

        </form>
    </div>
<!--  <div>{{ info }}</div>-->
  <BlogFooter/>
</template>

<script>

  import BlogHeader from '@/components/BlogHeader.vue'
  import BlogFooter from '@/components/BlogFooter.vue'

  import axios from 'axios';


    export default {
      name: 'ServiceTemp',
      components: {BlogHeader, BlogFooter},
      data: function () {
        return {
          service: null,
          msg: "hello world",
          qaTag: "init",
          nameResponse: "default"
        }
      },

      methods: {
        getNameResponde: function () {
          axios({
              method: 'post',
              url: '/recommand_qa',
              data: {"tag":this.qaTag},
              header:{
          'Content-Type':'application/json'  //如果写成contentType会报错
      }
            })

          // let data = {
          //   qaTag:"init"
          // }
          // data = JSON.stringify(data);  //数据转换成JSON
//           axios.get('https://192.168.190.63:5001/military_camp_recommand_service',
//               data,
//               {headers:{'Content-Type': 'application/json','Origin':"http://localhost:8080/"}}
// )
          // axios.get('https://192.168.190.63:5001/military_camp_recommand_service/?qaTag=init'
          // )
              .then(response => {
                this.nameResponse = response.data
                console.log(response)
              })
              .catch(error => {
                console.log(error)
              })
        },

        // mounted() {
        //   axios
        //       .get('https://api.coindesk.com/v1/bpi/currentprice.json')
        //       .then(response => (this.info = response))
        // },
        computed: {
          fullName: function () {
            return this.firstName + " " + this.lastName

          },
        }
      }
    }
</script>


<style scoped>

</style>