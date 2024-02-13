module.exports = {
  analize(req) {
    const agent = req.header('user-agent'); // User Agent we get from headers
    const referrer = req.header('referrer'); //  Likewise for referrer
    const ip = req.header('x-forwarded-for') || req.connection.remoteAddress; // Get IP - allow for proxy
    const screenWidth = req.param('width');
    const screenHeight = req.param('height');

    const response = { agent: agent, referrer: referrer, ip: ip, screenWidth: screenWidth, screenHeight: screenHeight };

    return response;
  },
};
