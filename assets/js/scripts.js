document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('userDetailsForm');
    const skillsInput = document.getElementById('skillsInput');
    const skillsContainer = document.getElementById('skillsContainer');
    const hiddenSkills = document.getElementById('skills');
    const resumeInput = document.getElementById('resume');
    const submitBtn = document.getElementById('submitBtn');
    let formSubmitted = false;
    let skillsList = [];

    // Add skill on Enter
    skillsInput.addEventListener('keydown', function (e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            const skill = skillsInput.value.trim();
            if (skill && !skillsList.includes(skill)) {
                skillsList.push(skill);
                renderSkills();
                skillsInput.value = '';
            }
        }
    });

    // Render skills
    function renderSkills() {
        skillsContainer.innerHTML = '';
        skillsList.forEach((skill, index) => {
            const skillTag = document.createElement('span');
            skillTag.className = 'skill-tag';
            skillTag.textContent = skill;

            const removeBtn = document.createElement('button');
            removeBtn.className = 'remove-skill';
            removeBtn.innerHTML = '&times;';
            removeBtn.addEventListener('click', () => {
                skillsList.splice(index, 1);
                renderSkills();
            });

            skillTag.appendChild(removeBtn);
            skillsContainer.appendChild(skillTag);
        });

        updateSkillsHiddenInput();
    }

    // Update hidden input
    function updateSkillsHiddenInput() {
        hiddenSkills.value = skillsList.join(', ');
    }

    // Form submission
    form.addEventListener('submit', function (e) {
        e.preventDefault();

        if (formSubmitted) return;

        updateSkillsHiddenInput();  // Ensure skills field is up-to-date

        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        const requiredFields = [
            'fullName', 'gender', 'dob', 'email', 'phone',
            'address', 'education', 'graduationYear', 'skills',
            'experience', 'jobRole', 'relocate'
        ];

        let isValid = true;

        requiredFields.forEach(field => {
            const value = data[field];
            if (!value || value.trim() === '') {
                isValid = false;
                const input = form.querySelector(`[name="${field}"]`);
                if (input) {
                    input.style.borderColor = 'red';
                    input.addEventListener('input', function () {
                        this.style.borderColor = '#ddd';
                    });
                }
            }
        });

        if (!isValid) {
            alert('Please fill all required fields');
            return;
        }

        // Email format check
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(data.email)) {
            alert('Please enter a valid email address');
            return;
        }

        // Phone validation
        if (data.phone.length < 8) {
            alert('Please enter a valid phone number');
            return;
        }

        // Resume check
        if (resumeInput.files.length === 0) {
            alert('Please upload a resume');
            return;
        } else {
            const file = resumeInput.files[0];
            const validTypes = [
                'application/pdf',
                'application/msword',
                'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            ];

            if (!validTypes.includes(file.type)) {
                alert('Please upload a PDF or Word document');
                return;
            }

            if (file.size > 5 * 1024 * 1024) {
                alert('File size should be less than 5MB');
                return;
            }
        }

        // All checks passed
        formSubmitted = true;
        submitBtn.disabled = true;
        submitBtn.textContent = 'Submitting...';

        // Optional: save to sessionStorage
        sessionStorage.setItem('formData', JSON.stringify(data));

        setTimeout(() => {
            form.submit();  // Actually submit to backend
        }, 1000);
    });
});