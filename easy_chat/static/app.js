'use strict'

;((g) => {
  const ws = new g.WebSocket(
    'ws://' + document.domain + ':' + document.location.port + '/ws/'
  )

  const messageTemplateEl = document.getElementById('message-template')
  function createMessageElem ({ username, text, timestamp }) {
    const messageEl = messageTemplateEl.cloneNode(true)
    messageEl.style.display = null

    const ts = new Date(timestamp)
    messageEl.querySelector('.username').innerText = username
    messageEl.querySelector('.timestamp').innerText = ts.toLocaleString('en-US')
    messageEl.querySelector('.text').innerText = text

    return messageEl
  }

  const messagesContainerEl = document.getElementById('messages')
  function appendMessages ({ messages }) {
    return messages
      .map(createMessageElem)
      .map(msgEl => messagesContainerEl.appendChild(msgEl))
  }

  ws.onmessage = (ev) => {
    const data = JSON.parse(ev.data)
    switch (data.type) {
      case 'messages': {
        const msgElems = appendMessages(data)
        const latestMsgEl = msgElems[msgElems.length - 1]
        latestMsgEl.scrollIntoView({ behavior: 'smooth' })
        break
      }

      default:
        throw new Error(`Unknown message type: ${data.type}`)
    }
  }

  const messageTextFieldEl = document.getElementById('message-text-field')
  const messageFormEl = document.getElementById('message-form')

  if (messageTextFieldEl && messageFormEl) {
    messageFormEl.addEventListener('submit', (ev) => {
      ev.preventDefault()

      const message = {
        username: user.username,
        text: messageTextFieldEl.value
      }
      ws.send(JSON.stringify(message))
      messageTextFieldEl.value = ''
    })
  }
})(window)
