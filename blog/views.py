from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True).order_by('-created_at')


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save(update_fields=["views"])
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['can_manage_blog'] = user.has_perm('blog.can_manage_blog')
        return context


class BlogCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published']
    template_name = 'blog/blog_form.html'

    def get_success_url(self):
        return reverse_lazy('blog:detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        user = self.request.user
        return user.has_perm('blog.can_manage_blog')


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:list')

    def test_func(self):
        return self.request.user.has_perm('blog.can_manage_blog')
