<template>
  <v-container grid-list-xl text-xs-center>
    <v-layout row wrap>
      <v-flex xs10 offset-xs1>
        <v-list two-line>
          <v-subheader>Overview</v-subheader>
          <template v-for="(item, index) in filteredList">
            <v-divider inset></v-divider>
            <v-list-tile avatar :key="item.title" @click="">
              <v-chip class="grey lighten-1" text-color="white">{{item.cost}} NOK</v-chip>
              <v-list-tile-content class='mx-3'>
                <v-list-tile-title v-html="item.title"></v-list-tile-title>
              </v-list-tile-content>
              <v-btn color="primary" dark v-if="item.resolve" :to="{name:'ExpenseList'}">Complete
                <v-icon dark right>check_circle</v-icon>
              </v-btn>
              <v-chip label outline :color="item.color" :text-color="item.color">{{item.pendingStatus}}</v-chip>
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
          pendingStatus: 'Pending',
          color:'grey',
          title: 'Europa Trip - 2 days',
          cost: '1000'
        },
        {
          pendingStatus: 'Ongoing',
          color:'blue',
          title: 'Europa Trip - 2 days',
          cost: '1000'
        },
        {
          pendingStatus: 'Completed',
          color:'green',
          title: '2000 post-its',
          cost: '2500'
        },
        {
          pendingStatus: 'Rejected',
          color:'red',
          title: 'Lunch money for the Spaceberg Team',
          cost: '4000'
        },
      ]
    }),
    computed: {
      filteredList() {
        return this.items.filter(item => {
          if (item.pendingStatus == 'Ongoing') {
            item.resolve = true
          }
          return item.title.toLowerCase().includes(this.search.toLowerCase())
        })
      }
    },
    props: ['search']
  }
</script>


