// ✅ 1. FORM VALIDATION FUNCTION
function validateForm() {
    let isValid = true;
    let email = document.getElementById('mail').value.trim();
    let name = document.getElementById('name').value.trim();
    let rating = document.getElementById('rating').value.trim();

    let mailError = document.getElementById('mailError');
    let ratingError = document.getElementById('ratingError');
    let nameError = document.getElementById('nameError');

    if (name === "") {
        nameError.textContent = "This field is required";
        isValid = false;
    } else {
        nameError.textContent = "";
    }

    if (email === "") {
        mailError.textContent = "This field is required";
        isValid = false;
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        mailError.textContent = "Enter a valid email";
        isValid = false;
    } else {
        mailError.textContent = "";
    }

    if (rating === "") {
        ratingError.textContent = "This field is required";
        isValid = false;
    } else if (rating > 5 || rating < 1) {
        ratingError.textContent = "Rating must be in between 1 and 5";
        isValid = false;
    } else {
        ratingError.textContent = "";
    }


    return isValid;
}

document.addEventListener('DOMContentLoaded', () => {
    // ✅ 2. CHART DRAWING CODE
    const ratingData = JSON.parse(document.getElementById('chart-data').textContent);

    const labels = Object.keys(ratingData).map(key => `${key} Stars`);
    const values = Object.values(ratingData);

    const colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'];

    new Chart(document.getElementById('barChart'), {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Number of Ratings',
                data: values,
                backgroundColor: colors
            }]
        }
    });

    new Chart(document.getElementById('pieChart'), {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                data: values,
                backgroundColor: colors
            }]
        }
    });
});
