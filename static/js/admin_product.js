document.addEventListener('DOMContentLoaded', function() {
  const nameInput = document.getElementById('id_name');
  const slugInput = document.getElementById('id_slug');

  nameInput.addEventListener('input', function() {
      const nameValue = nameInput.value;
      const slugValue = nameValue
          .toLowerCase()
          .replace(/[^a-zA-Z0-9\s]/g, '')
          .replace(/\s+/g, '-')
          .replace(/-+/g, '-');
      slugInput.value = slugValue;
  });
});