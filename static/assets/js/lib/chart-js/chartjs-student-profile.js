( function ( $ ) {
    "use strict";
    //Student History
    var ctx = document.getElementById( "student-history" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'line',
        data: {
            labels: [ "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre" ],
            type: 'line',
            defaultFontFamily: 'Montserrat',
            datasets: [ {
                label: "Ciencia, Tecnología y Ambiente",
                data: [ 18, 16, 16, 16, 17, 18, 19 ],
                backgroundColor: 'transparent',
                borderColor: 'rgba(220,53,69,0.75)',
                borderWidth: 3,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(220,53,69,0.75)',
                    }, {
                label: "Lengua y Literatura",
                data: [ 15, 16, 18, 16, 17, 18, 15 ],
                backgroundColor: 'transparent',
                borderColor: 'rgba(40,167,69,0.75)',
                borderWidth: 3,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(40,167,69,0.75)',
                    }, {
                label: "Matemáticas Aplicadas",
                data: [ 11, 12, 12, 11, 14, 13, 12 ],
                backgroundColor: 'transparent',
                borderColor: 'rgba(85,25,100,0.75)',
                borderWidth: 3,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(85,25,100,0.75)',
                    }, {
                label: "Talleres",
                data: [ 16, 15, 15, 16, 15, 16, 16 ],
                backgroundColor: 'transparent',
                borderColor: 'rgba(1,25,25,0.75)',
                borderWidth: 3,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(1,25,25,0.75)',
                    }, {
                label: "Razonamiento Matemático",
                data: [ 10, 12, 13, 15, 15, 15, 16 ],
                backgroundColor: 'transparent',
                borderColor: 'rgba(255,76,76,0.75)',
                borderWidth: 3,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(255,76,76,0.75)',
                    }, {
                label: "Razonamiento Verbal",
                data: [ 14, 15, 14, 15, 14, 14, 14 ],
                backgroundColor: 'transparent',
                borderColor: 'rgba(101,255,210,0.75)',
                borderWidth: 3,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(101,255,210,0.75)',
                    }, {
                label: "Ciencias Sociales",
                data: [ 13, 13, 13, 13, 13, 13, 13 ],
                backgroundColor: 'transparent',
                borderColor: 'rgba(255,234,53,0.75)',
                borderWidth: 3,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(255,234,53,0.75)',
                    } ]
        },
        options: {
            responsive: true,

            tooltips: {
                mode: 'index',
                titleFontSize: 12,
                titleFontColor: '#000',
                bodyFontColor: '#000',
                backgroundColor: '#fff',
                titleFontFamily: 'Montserrat',
                bodyFontFamily: 'Montserrat',
                cornerRadius: 3,
                intersect: false,
            },
            legend: {
                display: true,
                labels: {
                    usePointStyle: true,
                    fontFamily: 'Montserrat',
                },
            },
            scales: {
                xAxes: [ {
                    display: true,
                    gridLines: {
                        display: true,
                        drawBorder: true
                    },
                    scaleLabel: {
                        display: false,
                        labelString: 'Mes'
                    }
                        } ],
                yAxes: [ {
                    display: true,
                    gridLines: {
                        display: false,
                        drawBorder: false
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Promedio de Notas'
                    }
                        } ]
            },
            title: {
                display: false,
                text: 'Normal Legend'
            }
        }
    } );


    //Average Courses
    var ctx = document.getElementById( "average-courses" );
    ctx.height = 320;
    var myChart = new Chart( ctx, {
        type: 'radar',
        data: {
            labels: [ "Ciencia, Tecnología y Ambiente", "Lengua y Literatura", "Matemáticas Aplicadas", "Talleres", "Razonamiento Matemático", "Razonamiento Verbal", "Ciencias Sociales" ],
            datasets: [
                {
                    label: "Primer Trimestre",
                    data: [ 15, 10, 16, 17, 13, 11, 16 ],
                    borderColor: "rgba(0, 194, 146, 0.6)",
                    borderWidth: "1",
                    backgroundColor: "rgba(0, 194, 146, 0.4)"
                            },
                {
                    label: "Segundo Trimestre",
                    data: [ 17, 16, 17, 11, 13, 16, 14 ],
                    borderColor: "rgba(255, 16, 0, 0.7)",
                    borderWidth: "1",
                    backgroundColor: "rgba(255, 16, 0, 0.4)"
                            }
                        ]
        },
        options: {
            legend: {
                position: 'top'
            },
            scale: {
                ticks: {
                    beginAtZero: true
                }
            }
        }
    });


} )( jQuery );