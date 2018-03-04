<template>
  <v-container grid-list-xl text-xs-center>
    <v-layout row wrap>
      <v-flex xs10 offset-xs1>
        <v-list two-line>
          <v-subheader>Overview</v-subheader>
          <template v-for="(item, index) in filteredList">
            <v-divider inset></v-divider>
            <v-list-tile avatar :key="item.title" @click="">
              <v-chip class="grey darken-1" text-color="white">{{item.cost}} NOK</v-chip>
              <v-list-tile-content class='mx-3'>
                <v-list-tile-title v-html="item.title"></v-list-tile-title>
              </v-list-tile-content>
              <v-tooltip bottom>
                <v-icon dark color="orange darken-2" slot="activator" v-if='item.approval'>info</v-icon>
                <span>Requires approval</span>
              </v-tooltip>
              <v-btn color="primary" dark>Request
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
          title: 'Europa Trip - 2 days',
          approval: true,
          cost: '1000'
        },
        {
          title: 'Europa Trip - 4 days',
          approval: true,
          cost: '2500'
        },
        {
          title: 'Office Supplies',
          approval: false,
          cost: '200'
        },
        {
          title: 'Customs',
          approval: true,
          cost: '4000'
        },
        {
          title: 'Car leasing',
          approval: false,
          cost: '1000'
        },
      ]
    }),
    computed: {
      filteredList() {
        return this.items.filter(item => {
          return item.title.toLowerCase().includes(this.search.toLowerCase())
        })
      }
    },
    props: ['search']
  }
</script>
