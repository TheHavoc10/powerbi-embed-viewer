window.addEventListener('DOMContentLoaded', () => {
    fetch('/getEmbedToken')
        .then(response => response.json())
        .then(data => {
            const models = window['powerbi-client'].models;
            const config = {
                type: 'report',
                tokenType: models.TokenType.Embed,
                accessToken: data.token,
                embedUrl: `https://app.powerbi.com/reportEmbed?reportId=${data.reportId}&groupId=${data.groupId}`,
                id: data.reportId,
                settings: {
                    panes: {
                        filters: { visible: true },
                        pageNavigation: { visible: true }
                    },
                    bars: {
                        statusBar: { visible: true }
                    }
                }
            };
            const embedContainer = document.getElementById("embedContainer");
            const report = powerbi.embed(embedContainer, config);
            report.on("loaded", () => console.log("✅ Informe cargado"));
            report.on("rendered", () => console.log("📊 Informe renderizado"));
            report.on("error", event => console.error("❌ Error:", event.detail));
        })
        .catch(error => console.error("❌ Error al obtener el token:", error));
});
