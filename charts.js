function Charts(X,Y){
    const data = {
        labels: ['january','feb','mar'],
        datasets: [{
            label: "X-Axis",
            data: Y,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    };
    
    const config = {
        type: 'bar',
        data ,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    };
    const barChart = new Chart(document.getElementById('barChart').getContext('2d'),
    config
    );
    const config2 = {
        type: 'line',
        data ,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    };
    const lineChart = new Chart(document.getElementById('lineChart').getContext('2d'),
    config2
    );
    const config3 = {
        type: 'scatter',
        data ,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    };
    const pieChart = new Chart(document.getElementById('scatterChart').getContext('2d'),
    config3
    );
    
    }