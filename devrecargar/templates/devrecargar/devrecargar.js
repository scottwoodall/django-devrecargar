(function () {
    var source = new EventSource("{% url "devrecargar:ping" %}");
    var isFirstConnect = true;

    source.addEventListener("open", function () {
        if ( ! isFirstConnect) {
            console.log("devrecargar: reloading");
            location.reload();
        }

        isFirstConnect = false;
    }, false);
})();
