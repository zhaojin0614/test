import request from '../utils/requests'

export function getmsg (params) {
  return request({
    url: '/hello',
    method: 'get',
    params
  })
}
