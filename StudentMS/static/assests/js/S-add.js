document.addEventListener('DOMContentLoaded', function() {
  // File upload display
  const fileInput = document.getElementById('profile_pic');
  const fileNameDisplay = document.getElementById('file-name');
  
  fileInput.addEventListener('change', function() {
    if (this.files.length > 0) {
      fileNameDisplay.textContent = this.files[0].name;
    } else {
      fileNameDisplay.textContent = 'No file chosen';
    }
  });

  // Form validation
  const form = document.getElementById('studentForm');
  const nameInput = document.getElementById('full_name');
  const rollInput = document.getElementById('roll_number');
  const gpaInput = document.getElementById('gpa');
  
  nameInput.addEventListener('input', validateName);
  rollInput.addEventListener('input', validateRollNumber);
  gpaInput.addEventListener('input', validateGPA);
  
  function validateName() {
    const nameError = document.getElementById('name-error');
    if (nameInput.value.length < 3) {
      nameError.textContent = 'Name must be at least 3 characters';
      return false;
    } else if (!/^[a-zA-Z\s]+$/.test(nameInput.value)) {
      nameError.textContent = 'Name can only contain letters and spaces';
      return false;
    } else {
      nameError.textContent = '';
      return true;
    }
  }
  
  function validateRollNumber() {
    const rollError = document.getElementById('roll-error');
    if (!/^[A-Z]{2,4}-\d{3}$/.test(rollInput.value)) {
      rollError.textContent = 'Format: ABC-123 (e.g., BSCS-001)';
      return false;
    } else {
      rollError.textContent = '';
      return true;
    }
  }
  
  function validateGPA() {
    const gpaError = document.getElementById('gpa-error');
    const gpaValue = parseFloat(gpaInput.value);
    
    if (isNaN(gpaValue) || gpaValue < 0 || gpaValue > 4) {
      gpaError.textContent = 'GPA must be between 0 and 4';
      return false;
    } else {
      gpaError.textContent = '';
      return true;
    }
  }
  
  // Form submission
  form.addEventListener('submit', function(e) {
    e.preventDefault();
    
    const isNameValid = validateName();
    const isRollValid = validateRollNumber();
    const isGPAValid = validateGPA();
    
    if (isNameValid && isRollValid && isGPAValid) {
      // Simulate form submission
      showNotification('Student added successfully!', 'success');
      
      // Reset form
      form.reset();
      fileNameDisplay.textContent = 'No file chosen';
      
      // In a real app, you would submit the form data to the server here
      // setTimeout(() => { form.submit(); }, 1500);
    } else {
      showNotification('Please fix the errors in the form', 'error');
    }
  });
  
  // Notification function
  function showNotification(message, type) {
    const notification = document.getElementById('notification');
    notification.textContent = message;
    notification.className = `notification ${type}`;
    
    setTimeout(() => {
      notification.classList.add('show');
    }, 10);
    
    setTimeout(() => {
      notification.classList.remove('show');
    }, 3000);
  }
});