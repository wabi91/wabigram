

export default {
  Query: {
    sayHello: async (_, args, { prisma }) => {
      const res = await prisma.user.count(); 
      console.log(res);
      return 'hello~!';
    },
  },
}