document.addEventListener("DOMContentLoaded", function () {
    var scrollLinks = document.querySelectorAll(".nav-link");

    for (var i = 0; i < scrollLinks.length; i++) {
        scrollLinks[i].addEventListener("click", smoothScroll);
    }

    function smoothScroll(event) {
        var targetId = this.getAttribute("href");

        // Check if the target is a hash link
        if (targetId.startsWith('#')) {
            event.preventDefault(); // Prevent default only for hash links
            var targetPosition = document.querySelector(targetId).offsetTop;
            window.scrollTo({
                top: targetPosition,
                behavior: "smooth",
            });
        } else {
            // Allow default behavior for other links (like /roadmap/)
            window.location.href = targetId;
        }
    }
    document.addEventListener("DOMContentLoaded", function () {
        var scrollLinks = document.querySelectorAll(".nav-link");
    
        for (var i = 0; i < scrollLinks.length; i++) {
            scrollLinks[i].addEventListener("click", smoothScroll);
        }
    
        function smoothScroll(event) {
            var targetId = this.getAttribute("href");
    
            // Check if the target is a hash link
            if (targetId.startsWith('#')) {
                event.preventDefault(); // Prevent default only for hash links
                var targetPosition = document.querySelector(targetId).offsetTop;
                window.scrollTo({
                    top: targetPosition,
                    behavior: "smooth",
                });
            } else {
                // Allow default behavior for other links (like /roadmap/)
                window.location.href = targetId;
            }
        }
    });
    var getRecipesButton = document.getElementById("get-recipes-button");
    
    if (getRecipesButton) {
        getRecipesButton.addEventListener("click", function () {
            setTimeout(function () {
                var recommendationSection = document.getElementById("recommendation");
                if (recommendationSection) {
                    recommendationSection.scrollIntoView({ behavior: "smooth" });
                }
            }, 500); // Adjust the delay if necessary
        });
    }
    
});