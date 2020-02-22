import _ from 'lodash';
import {
  GET_USERS,
  GET_USER,
  ADD_USER,
  DELETE_USER,
  EDIT_USER
} from '../actions/types';

export default (state = {}, action) => {
  switch (action.type) {
    case GET_USERS:
      return {
        ...state,
        ..._.mapKeys(action.payload, 'id')
      };
    case GET_USER:
    case ADD_USER:
    case EDIT_USER:
      return {
        ...state,
        [action.payload.id]: action.payload
      };
    case DELETE_USER:
      return _.omit(state, action.payload);
    default:
      return state;
  }
};
