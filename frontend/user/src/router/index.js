import Vue from 'vue'
import Router from 'vue-router'
import Overview from '@/components/Overview'
import FundingRequest from '@/components/FundingRequest'
import ExpenseList from '@/components/ExpenseList'
import Success from '@/components/Success'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Overview',
      component: Overview,
    },
    {
      path: '/fundingrequest',
      name: 'FundingRequest',
      component: FundingRequest,
    },
    {
      path: '/expenselist',
      name: 'ExpenseList',
      component: ExpenseList,
    },
    {
      path: '/success',
      name: 'Success',
      component: Success,
    }
  ]
})
