/* globals Chart:false, feather:false */

(function () {
  'use strict'

  feather.replace();

  // Graphs
  var ctx = document.getElementById('myChart');
  var quantity = document.querySelector('main');
  console.log(quantity.dataset.apiary);
  // eslint-disable-next-line no-unused-vars
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: [
        'Apiary',
        'BeeHive',
        'BeeFamily',
        'BeeMother',
      ],
      datasets: [{
        data: [
          quantity.dataset.apiary,
          quantity.dataset.beehive,
          quantity.dataset.beefamily,
          quantity.dataset.mother,
        ],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  })
}())
