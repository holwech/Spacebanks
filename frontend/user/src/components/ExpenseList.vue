<template>
  <v-container grid-list-xl text-xs-center>
    <v-layout row wrap>
      <v-flex xs10 offset-xs1>
        <v-list two-line>
          <template>
            <v-list two-line subheader>
              <v-subheader>Select related transactions</v-subheader>
              <v-divider inset></v-divider>
              <v-list-tile avatar v-for="(item, index) in filteredList" :key='item.id'>
                <v-list-tile-action>
                  <v-checkbox v-model="checkedTrans" :value='item.id'></v-checkbox>
                </v-list-tile-action>
                <v-chip class="grey lighten-1" text-color="white">{{item.cost}} NOK</v-chip>
                <v-list-tile-content class='mx-3'>
                  <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                  <v-list-tile-sub-title>{{ item.datetime }}</v-list-tile-sub-title>
                </v-list-tile-content>
              </v-list-tile>
            </v-list>
            <v-divider inset></v-divider>
            <v-list-tile avatar @click="">
              <v-list-tile-content class='mx-3'>
                <v-list-tile-title>
                  <h2 class="headline mb-0">Total</h2>
                </v-list-tile-title>
              </v-list-tile-content>
              <v-card-title primary-title >
                <div>
                  <h2 class="headline mb-0">{{ total }} NOK</h2>
                </div>
              </v-card-title>
            </v-list-tile>
            <v-list-tile avatar @click="">
              <v-list-tile-content class='mx-3'>
                <v-list-tile-title>
                </v-list-tile-title>
              </v-list-tile-content>
              <v-card-title primary-title >
                <v-btn color="primary" dark class='mx-1' :to="{name:'Success'}">Finish
                  <v-icon dark right>check_circle</v-icon>
                </v-btn>
              </v-card-title>
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
      checkedTrans: [ ],
      items: [
        {
          id: '1',
          title: "Netflix subscription",
          cost: 399,
          datetime: '27. March'
        },
        {
          id: '2',
          title: "Clarion Hotel",
          cost: 689,
          datetime: '27. March'
        },
        {
          id: '3',
          title: "Norwegian to Trondheim",
          cost: 1499,
          datetime: '26. March'
        },
        {
          id: '4',
          title: "Prinsen Kino",
          cost: 119,
          datetime: '26. March'
        },
      ]
    }),
    computed: {
      filteredList() {
        return this.items.filter(item => {
          return item.title.toLowerCase().includes(this.search.toLowerCase())
        })
      },
      total() {
        var filtered = this.items.filter(item => {
          return this.checkedTrans.includes(item.id)
        }, this);
        var sum = 0;
        for (var i = 0; i < filtered.length; i++) {
          sum += filtered[i].cost
        }
        return sum
      }
    },
    props: ['search']
  }
</script>


