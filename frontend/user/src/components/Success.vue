<template>
  <v-container grid-list-xl text-xs-center>
    <v-layout row wrap>
      <v-flex xs10 offset-xs1>
        <v-card class='pa-5' :to="{name:'Success'}">
          <v-card-title primary-title>
            <v-layout row justify-space-around>
            <div>
              <h1 class="headline mb-0">Success <v-icon color='green'>check</v-icon></h1>
            </div>
            </v-layout>
          </v-card-title>
        </v-card>
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


