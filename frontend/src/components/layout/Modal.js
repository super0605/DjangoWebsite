import React from 'react';
import ReactDOM from 'react-dom';

const Modal = (props) => {
  console.log('hello world')
  console.log(props)
  console.log('props')
  console.log('props2')
  console.log('test')
  return ReactDOM.createPortal(
    <div onClick={props.onDismiss} className='ui active dimmer'>
      <div onClick={e => e.stopPropagation()} className='ui active modal'>
        <div className='header'>{props.title}</div>
        <div className='content'>{props.content}</div>
        <div className='actions'>{props.actions}</div>
      </div>
    </div>,
    document.querySelector('#modal')
  );
};


export default Modal;
