document.addEventListener('DOMContentLoaded', () => {
  const tbody = document.querySelector("tbody");
  const originalRowsHTML = tbody.innerHTML;
  const resultData = window.results || [];

  // Build chart
  const labels = resultData.map(item => item[0]);
  const scores = resultData.map(item => Math.round(item[1] * 10000) / 100);

  const ctx = document.getElementById('scoreChart').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Match Score (%)',
        data: scores,
        backgroundColor: 'rgba(54, 162, 235, 0.6)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      plugins: {
        tooltip: {
          callbacks: {
            label: (context) => `${context.raw}%`
          }
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          max: 100,
          title: {
            display: true,
            text: 'Score (%)'
          }
        },
        x: {
          ticks: {
            maxRotation: 60,
            minRotation: 30,
            autoSkip: false
          }
        }
      }
    }
  });

  // Filter logic
  const rows = document.querySelectorAll("tbody tr");
  const roleSet = new Set();

  rows.forEach(row => {
    const role = row.querySelector("td:nth-child(7)")?.textContent.trim();
    if (role && role !== "—") roleSet.add(role);
  });

  const roleFilter = document.getElementById("roleFilter");
  const scoreFilter = document.getElementById("scoreFilter");
  const searchInput = document.getElementById("searchInput");

  if (roleFilter) {
    roleSet.forEach(role => {
      const opt = document.createElement("option");
      opt.value = opt.textContent = role;
      roleFilter.appendChild(opt);
    });
  }

  function applyFilters() {
    const selectedRole = roleFilter?.value || "";
    const minScore = parseFloat(scoreFilter?.value || "0");
    const searchTerm = searchInput?.value.toLowerCase() || "";

    rows.forEach(row => {
      const role = row.querySelector("td:nth-child(7)")?.textContent.trim();
      const scoreText = row.querySelector("td:nth-child(2)")?.textContent.replace('%', '').trim() || "0";
      const score = parseFloat(scoreText);
      const text = row.textContent.toLowerCase();

      const matchRole = !selectedRole || role === selectedRole;
      const matchScore = score >= minScore;
      const matchSearch = text.includes(searchTerm);

      row.style.display = matchRole && matchScore && matchSearch ? "" : "none";
    });
  }

  roleFilter?.addEventListener("change", applyFilters);
  scoreFilter?.addEventListener("input", applyFilters);
  searchInput?.addEventListener("input", applyFilters);

  // Sorting logic for Match Score (single toggle button)
  const sortBtn = document.getElementById("sortScoreToggle");
  const sortIcon = document.getElementById("sortScoreIcon");
  let sortState = 2; // 0: desc, 1: asc, 2: default (so first click is descending)

  function sortTableByScore(ascending = true) {
    const rows = Array.from(tbody.querySelectorAll("tr"));
    rows.sort((a, b) => {
      const scoreA = parseFloat(a.cells[1].textContent.replace('%', '').trim());
      const scoreB = parseFloat(b.cells[1].textContent.replace('%', '').trim());
      return ascending ? scoreA - scoreB : scoreB - scoreA;
    });
    rows.forEach(row => tbody.appendChild(row));
  }

  function resetTableOrder() {
    tbody.innerHTML = originalRowsHTML;
  }

  sortBtn?.addEventListener("click", () => {
    sortState = (sortState + 1) % 3;
    if (sortState === 0) {
      sortTableByScore(false); // Descending
      sortIcon.innerHTML = "&#9660;"; // Down arrow
    } else if (sortState === 1) {
      sortTableByScore(true); // Ascending
      sortIcon.innerHTML = "&#9650;"; // Up arrow
    } else {
      resetTableOrder();
      sortIcon.innerHTML = "&#8597;"; // Up/down arrow
    }
  });
});
