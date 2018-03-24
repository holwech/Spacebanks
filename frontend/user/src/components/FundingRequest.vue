<template>
  <v-container grid-list-xl text-xs-center>
    <v-layout row wrap>
      <v-flex xs10 offset-xs1>
        <v-list two-line>
          <v-subheader>Overview</v-subheader>
          <template v-for="(item, index) in filteredList">
            <v-divider inset></v-divider>
            <v-list-tile avatar :key="item.id" @click="">
              <v-chip class="grey lighten-1" text-color="white">{{item.cost}} NOK</v-chip>
              <v-list-tile-content class='mx-3'>
                <v-list-tile-title v-html="item.title"></v-list-tile-title>
              </v-list-tile-content>
              <v-tooltip bottom>
                <v-icon dark color="orange darken-2" slot="activator" v-if='item.approval'>info</v-icon>
                <span>Requires approval</span>
              </v-tooltip>
              <v-btn color="grey lighten-1" dark @click="submitRequest" :to="{name:'Success'}">Request
                <v-icon dark right>check_circle</v-icon>
              </v-btn>
            </v-list-tile>
          </template>
        </v-list>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  export default {
    data: () => ({
      items: [
        {
          id: '1',
          title: 'Europe Trip - 2 days',
          approval: true,
          cost: '1000'
        },
        {
          id: '2',
          title: 'Europe Trip - 4 days',
          approval: true,
          cost: '2500'
        },
        {
          id: '3',
          title: 'Office Supplies',
          approval: false,
          cost: '200'
        },
        {
          id: '4',
          title: 'Customs',
          approval: true,
          cost: '4000'
        },
        {
          id: '5',
          title: 'Car leasing',
          approval: false,
          cost: '1000'
        },
      ]
    }),
    methods: {
      submitRequest(event) {
        console.log("Click!")
        this.loading = true
        this.axios({
          method: 'post',
          url: 'http://localhost:5555/getfundingtypes/',
          data: {
            'user_id': '14115374012'
          },
        }).then(response => {
         this.items = response.data
        }, this).catch(error => {
          console.log('AJAX FAILED: ' + error)
        })
      },
    },
    beforeCreate () {
      const api = `http://localhost:3000/urls?id=${this.$route.params.urlId}`
      this.axios.get(api).then(response => {
        this.item = response.data[0]
      }).catch(error => {
        console.log('AJAX FAILED: ' + error)
      })
    },
    computed: {
      filteredList() {
        return this.items.filter(item => {
          var selected = item.title.toLowerCase().includes(this.search.toLowerCase())
          if (selected) {
            item.clicked = true
          }
          return selected
        })
      }
    },
    props: ['search']
  }
</script>
