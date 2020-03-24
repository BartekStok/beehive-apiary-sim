/* globals Chart:false, feather:false */
$(document).ready(function () {
  $.ajax({
    url: "http://127.0.0.1:8000/beehive_view/",
    data: {},
    type: "GET",
    // dataType: "json"
  }).done(function (result) {
    console.log((result));
  });
});

(function () {
  'use strict';

  feather.replace();

  // Graphs
  var ctx = document.getElementById('myChart')
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
          1,
          5,
          5,
          5,
          5,
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
}());
