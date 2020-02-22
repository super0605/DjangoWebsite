import _ from 'lodash';
import React, { Component } from "react";
import { Link, Redirect } from "react-router-dom";
import { connect } from "react-redux";
import { getUser, editUser } from "../../actions/users";
import ProfileForm from './ProfileForm';

class Profile extends Component {

  componentDidMount() {
    this.props.getUser(this.props.match.params.id);
  }

  onSubmit = formValues => {
    this.props.editUser(this.props.match.params.id, formValues);
  };

  handleUserType = (is_student, is_teacher) => {
    let user_type = ''
    if (!!is_student) {
      user_type = 'is_student'
    } else if (!!is_teacher) {
      user_type = 'is_teacher'
    } else {
      user_type = ''
    }
    return user_type;
  }

  render() {
    const { user } = this.props
    const initialValues = _.pick(user, ['username', 'email'])
    initialValues.user_type = this.handleUserType(user ? user.is_student : '', user ? user.is_teacher : '')
    return (
      <>
        <ProfileForm 
          initialValues={initialValues}
          enableReinitialize={true}
        />
      </>
    );
  }
}

const mapStateToProps = (state, ownProps) => ({
  isAuthenticated: state.auth.isAuthenticated,
  user: state.users[ownProps.match.params.id],
});

export default connect(
  mapStateToProps,
  { getUser, editUser }
)(Profile);
