<template>
  <div id="app">
    <v-app id="inspire">
      <v-toolbar
        class="blue accent-3"
        dark
        tabs
      >
      <v-toolbar-title style="width: 300px" class="ml-0 pl-3">
          <span class="hidden-sm-and-down">BudgetTree</span>
          </v-toolbar-title>
                <v-text-field
                  prepend-icon="search"
                  label="Search"
                  solo-inverted
                  class="mx-3"
                  flat
                  v-model="search"
                ></v-text-field>
        <v-spacer></v-spacer>
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
            Request funding
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
