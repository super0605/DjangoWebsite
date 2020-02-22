import axios from 'axios';
import { reset } from 'redux-form';
import history from '../history';
import { tokenConfig } from './auth';
import { GET_USERS, GET_USER, ADD_USER, DELETE_USER, EDIT_USER } from './types';

// GET USERS
export const getUsers = () => async (dispatch, getState) => {
  const res = await axios.get('/api/auth/users/', tokenConfig(getState));
  dispatch({
    type: GET_USERS,
    payload: res.data
  });
};

// GET USER
export const getUser = id => async (dispatch, getState) => {
  const res = await axios.get(`/api/auth/users/${id}/`, tokenConfig(getState));
  dispatch({
    type: GET_USER,
    payload: res.data
  });
};

// ADD USER
export const addUser = formValues => async (dispatch, getState) => {
  const res = await axios.post(
    '/api/auth/users/',
    { ...formValues },
    tokenConfig(getState)
  );
  dispatch({
    type: ADD_USER,
    payload: res.data
  });
  dispatch(reset('todoForm'));
};

// DELETE USER
export const deleteUser = id => async (dispatch, getState) => {
  await axios.delete(`/api/auth/users/${id}/`, tokenConfig(getState));
  dispatch({
    type: DELETE_USER,
    payload: id
  });
  history.push('/');
};

// EDIT USER
export const editUser = (id, formValues) => async (dispatch, getState) => {
  const res = await axios.patch(
    `/api/auth/users/${id}/`,
    formValues,
    tokenConfig(getState)
  );
  dispatch({
    type: EDIT_USER,
    payload: res.data
  });
  history.push('/');
};
