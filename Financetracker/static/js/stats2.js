// Function to render Doughnut Chart for Income
console.log("stats2.js loaded");

const renderChart = (data, labels) => {
    var ctx = document.getElementById("incomeChart").getContext("2d");
    var myChart = new Chart(ctx, {
      type: "doughnut",
      data: {
        labels: labels,
        datasets: [
          {
            label: "Income per category",
            data: data,
            backgroundColor: [
              "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(255, 206, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(153, 102, 255, 0.2)",
              "rgba(255, 159, 64, 0.2)",
            ],
            borderColor: [
              "rgb(190, 38, 71)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(153, 102, 255, 1)",
              "rgba(255, 159, 64, 1)",
            ],
            borderWidth: 1,
          },
        ],
      },
      options: {
        title: {
          display: true,
          text: "Income per category",
        },
      },
    });
  };
  
  // Function to render Bar Chart for Income
  const renderChart2 = (data, labels) => {
    var ctx = document.getElementById("incomeChart2").getContext("2d");
    var myChart = new Chart(ctx, {
      type: "bar",
      data: {
        labels: labels,
        datasets: [
          {
            label: "Income per category",
            data: data,
            backgroundColor: [
              "rgb(255, 99, 132, 0.2)",
              "rgba(89, 143, 179, 0.2)",
              "rgba(239, 183, 39, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(153, 102, 255, 0.2)",
              "rgba(255, 159, 64, 0.2)",
            ],
            borderColor: [
              "rgba(255, 99, 132, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(153, 102, 255, 1)",
              "rgba(255, 159, 64, 1)",
            ],
            borderWidth: 1,
          },
        ],
      },
      options: {
        title: {
          display: true,
          text: "Income per category",
        },
      },
    });
  };

  // Fetch income data and render both charts
  const getChartData1 = () => {
    console.log("fetching income data");
    fetch("/income/income_category_summary")
      .then((res) => res.json())
      .then((results) => {
        console.log("Income data:", results);
        const category_data = results.income_category_data;
        const [labels, data] = [
          Object.keys(category_data),
          Object.values(category_data),
        ];
  
        renderChart(data, labels);  // Render doughnut chart
        renderChart2(data, labels); // Render bar chart
      });
  };
  
  // Trigger fetching and rendering of income charts
  
  document.onload = getChartData1();