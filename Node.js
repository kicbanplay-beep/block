const WebSocket = require("ws");
const PORT = process.env.PORT || 8080;

const server = new WebSocket.Server({ port: PORT });
let clients = [];

server.on("connection", (ws) => {
  clients.push(ws);
  ws.on("message", (msg) => {
    clients.forEach((client) => {
      if (client !== ws && client.readyState === WebSocket.OPEN) {
        client.send(msg.toString());
      }
    });
  });
  ws.on("close", () => {
    clients = clients.filter((c) => c !== ws);
  });
});

console.log("✅ WebSocket server запущен на порту " + PORT);
