document.addEventListener('DOMContentLoaded', () => {
    // Select all toggle buttons
    const toggleButtons = document.querySelectorAll('.toggle-btn');

    toggleButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Find the parent wrapper for this button
            const itemWrapper = button.closest('.item-wrapper');
            if (!itemWrapper) return; // Should not happen with current HTML structure

            // Find the expandable area within this wrapper
            const expandableArea = itemWrapper.querySelector('.expandable-area');
            if (!expandableArea) return; // Should not happen

            // Find the icon within the button
            const icon = button.querySelector('i');
            if (!icon) return; // Should not happen

            // Toggle the display of the expandable area
            const isHidden = expandableArea.style.display === 'none';
            if (isHidden) {
                expandableArea.style.display = 'block';
                icon.classList.remove('fa-plus');
                icon.classList.add('fa-minus');
            } else {
                expandableArea.style.display = 'none';
                icon.classList.remove('fa-minus');
                icon.classList.add('fa-plus');
            }
        });
    });
});
