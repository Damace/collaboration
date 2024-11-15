document.addEventListener('DOMContentLoaded', function () {
    const sponsorNameField = document.getElementById('id_sponsor_name'); // Adjust if necessary
    const optionalFields = [
        'id_mobile',
        'id_email',
        'id_postal_address',
        'id_physical_address',
    ];

    function toggleOptionalFields() {
        const selectedValue = sponsorNameField.options[sponsorNameField.selectedIndex].text;
        const isGovernment = selectedValue === 'Government'; // Default is Government

        optionalFields.forEach(fieldId => {
            const field = document.getElementById(fieldId);
            if (field) {
                field.closest('.form-row').style.display = isGovernment ? 'none' : 'block';
            }
        });
    }

    // Initial setup - check if "Government" is selected by default
    toggleOptionalFields();

    // Add event listener for changes
    sponsorNameField.addEventListener('change', toggleOptionalFields);
});
