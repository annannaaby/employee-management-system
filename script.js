let formFields = [];

function addField() {
    const label = document.getElementById('field-label').value;
    const type = document.getElementById('field-type').value;

    if (label && type) {
        formFields.push({ label, type });
        renderForm();
    }
}

function renderForm() {
    const preview = document.getElementById('form-preview');
    preview.innerHTML = '';

    formFields.forEach((field, index) => {
        const fieldHTML = `
            <div>
                <label>${field.label}</label>
                <input type="${field.type}" name="${field.label}">
            </div>`;
        preview.innerHTML += fieldHTML;
    });
}

function submitForm() {
    const employeeName = prompt('Enter Employee Name:');
    const dynamicData = {};

    formFields.forEach(field => {
        const value = document.querySelector(`input[name="${field.label}"]`).value;
        dynamicData[field.label] = value;
    });

    fetch('/api/employees/employees/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            name: employeeName,
            dynamic_data: dynamicData,
        }),
    })
    .then(response => response.json())
    .then(data => alert(data.message))
    .catch(err => console.error(err));
}
