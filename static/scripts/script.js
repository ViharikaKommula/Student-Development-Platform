document.addEventListener('DOMContentLoaded', function () {
    // Function to handle API requests
    async function makeRequest(url, data, containerId) {
      try {
        const response = await fetch(url, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(data),
        });
  
        if (!response.ok) {
          throw new Error(`Error: ${response.status}`);
        }
  
        const result = await response.json();
        document.getElementById(containerId).innerText = result.message;
      } catch (error) {
        console.error('An error occurred:', error.message);
        document.getElementById(containerId).innerText = 'An error occurred while processing your request.';
      }
    }
  
    // Event delegation using the closest() method
    document.addEventListener('click', function (event) {
      const target = event.target;
  
      if (target.closest('#trackAcademicBtn')) {
        makeRequest('/academics', { 
          subject: document.getElementById('subject').value,
          grade: document.getElementById('grade').value 
        }, 'academicResults');
      } else if (target.closest('#supportMentalHealthBtn')) {
        makeRequest('/mentalhealth', { 
          emotion: document.getElementById('emotion').value,
          activity: document.getElementById('activity').value 
        }, 'mentalHealthResults');
      } else if (target.closest('#exploreInterestsBtn')) {
        makeRequest('/interests', { 
          interest: document.getElementById('interest').value 
        }, 'interestsResults');
      } else if (target.closest('#getRecommendationBtn')) {
        makeRequest('/recommendations', { 
          academic_performance: document.getElementById('academic_performance').value,
          mental_health: document.getElementById('mental_health').value,
          interest: document.getElementById('interestRecommendation').value 
        }, 'recommendationResults');
      } else if (target.closest('#getSummaryBtn')) {
        makeRequest('/summary', {}, 'summaryResults');
      } else if (target.closest('#submitFeedbackBtn')) {
        makeRequest('/feedback', { 
          feedbackText: document.getElementById('feedbackText').value 
        }, 'feedbackResults');
      }
    });
  });
  