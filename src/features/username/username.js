import {createSlice} from '@reduxjs/toolkit'

const initialState = {
    usrname: ''
}

const usernameSlice = createSlice({
    name: 'username',
    initialState,
    reducers:{
        changed: (state, action) => {
            state.usrname = action.payload
        }
    }
})

export default usernameSlice.reducer
export const {changed} = usernameSlice.actions

