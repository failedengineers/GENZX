document.addEventListener("DOMContentLoaded", () => {
  const subjectItems = document.querySelectorAll(".subject-list li");

  subjectItems.forEach(item => {
    item.addEventListener("click", () => {
      const subjectId = item.dataset.subjectId;
      console.log("Selected subject:", subjectId);

      // Highlight selected subject
      subjectItems.forEach(li => li.classList.remove("active"));
      item.classList.add("active");

      // Navigate to resources page
      const url = `${window.location.origin}/resources/?subject_id=${subjectId}`;
      console.log("Navigating to:", url);
      window.location.assign(url); // forces navigation
    });
  });
});
