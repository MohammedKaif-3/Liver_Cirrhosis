document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.getElementById("menu-toggle");
  const nav = document.getElementById("nav-links");

  if (toggle && nav) {
    toggle.addEventListener("click", () => {
      if (nav.classList.contains("active")) {
        nav.style.opacity = 0;
        nav.style.transform = "translateY(-10px)";
        setTimeout(() => {
          nav.classList.remove("active");
        }, 300); // Match CSS transition duration
      } else {
        nav.classList.add("active");
        setTimeout(() => {
          nav.style.opacity = 1;
          nav.style.transform = "translateY(0)";
        }, 10); // Tiny delay to trigger transition
      }

      toggle.classList.toggle("open");
    });
  }
});


function fillDemo() {
    const demoData = {
        total_bilirubin_mg_dl: 1.4,
        duration_of_alcohol_consumption_years: 10,
        direct_mg_dl: 0.4,
        al_phosphatase_u_l: 210,
        platelet_count_lakhs_mm: 2.3,
        indirect_mg_dl: 1.0,
        polymorphs_percent: 62,
        albumin_g_dl: 3.6,
        pcv_percent: 40,
        sgot_ast_u_l: 120,
        lymphocytes_percent: 28,
        age: 45,
        monocytes_percent: 10,
        bp_systolic: 130,
        hemoglobin_g_dl: 13.2,
        quantity_of_alcohol_consumption_quarters_day: 2,
        diabetes_result: "Negative",
        total_protein_g_dl: 6.8,
        sgpt_alt_u_l: 98,
        globulin_g_dl: 3.2
    };

    for (let key in demoData) {
        const input = document.querySelector(`[name=${key}]`);
        if (input) input.value = demoData[key];
    }
}

document.addEventListener("DOMContentLoaded", () => {
  const chartElement = document.getElementById("featureChart");

  if (chartElement) {
    const featureData = JSON.parse(chartElement.dataset.importance);

    // Use 1-based index labels for the y-axis
    const indexLabels = featureData.labels.map((_, i) => (i + 1).toString());

    new Chart(chartElement, {
      type: "bar",
      data: {
        labels: indexLabels,
        datasets: [{
          label: "Feature Importance",
          data: featureData.values,
          backgroundColor: "#3366cc"
        }]
      },
      options: {
        indexAxis: 'y',
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: {
            beginAtZero: true,
            title: {
              display: true,
              text: 'Importance Score'
            },
            ticks: {
              font: {
                size: 12
              }
            }
          },
          y: {
            ticks: {
              font: {
                size: 12
              }
            },
            title: {
              display: true,
              text: 'Feature Index'
            }
          }
        },
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              // Show full feature name in tooltip
              title: (context) => {
                const index = context[0].dataIndex;
                return `(${index + 1}) ${featureData.labels[index]}`;
              }
            }
          }
        }
      }
    });
  }
});


