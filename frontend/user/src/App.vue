<template>
  <div id="app">
    <v-app id="inspire">
      <v-toolbar
        class="blue accent-3"
        dark
        tabs
      >
        <v-container grid-list-xl text-xs-center>
          <v-layout row wrap>
            <v-flex xs10 offset-xs1>
              <v-text-field
                prepend-icon="search"
                label="Search"
                solo-inverted
                class="mx-3"
                flat
                v-model="search"
              ></v-text-field>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
        <v-tabs
          slot="extension"
          centered
          v-model="tabs"
          slider-color="white"
          color="transparent"
        >
          <v-tab
            :to="{name:'Overview'}"
            >
            Overview
          </v-tab>
          <v-tab
            :to="{name:'FundingRequest'}"
            >
            Funding request
          </v-tab>
        </v-tabs>
      </v-toolbar>
      <v-content>
        <router-view :search="search"></router-view>
      </v-content>
    </v-app>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: () => ({
    search: '',
    tabsNames: [
      "Overview",
      "Request funding",
    ],
    dialog: false,
    drawer: null,
    items: [
      { icon: 'contacts', text: 'Contacts' },
      { icon: 'history', text: 'Frequently contacted' },
      { icon: 'content_copy', text: 'Duplicates' },
      {
        icon: 'keyboard_arrow_up',
        'icon-alt': 'keyboard_arrow_down',
        text: 'Labels',
        model: true,
        children: [
          { icon: 'add', text: 'Create label' }
        ]
      },
      {
        icon: 'keyboard_arrow_up',
        'icon-alt': 'keyboard_arrow_down',
        text: 'More',
        model: false,
        children: [
          { text: 'Import' },
          { text: 'Export' },
          { text: 'Print' },
          { text: 'Undo changes' },
          { text: 'Other contacts' }
        ]
      },
      { icon: 'settings', text: 'Settings' },
      { icon: 'chat_bubble', text: 'Send feedback' },
      { icon: 'help', text: 'Help' },
      { icon: 'phonelink', text: 'App downloads' },
      { icon: 'keyboard', text: 'Go to the old version' }
    ]
  }),
  props: {
    source: String
  }
}
</script>

<style scoped>
.mx-5
  margin-left: 5px !important
</style>
